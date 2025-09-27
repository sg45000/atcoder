use std::cmp::Ordering;

use crate::io::get_ints_n_lines;

mod io {
    use std::fmt::Debug;
    use std::io;
    use std::str::FromStr;

    /// 改行だけ落として1行返す（前後の空白はそのまま）
    fn read_line_no_newline() -> String {
        let mut s = String::new();
        io::stdin().read_line(&mut s).unwrap();
        s.trim_end_matches(&['\n', '\r'][..]).to_string()
    }

    pub fn get_int<T>() -> T
    where
        T: FromStr,
        T::Err: Debug,
    {
        read_line_no_newline().trim().parse::<T>().unwrap()
    }

    pub fn get_ints<T>() -> Vec<T>
    where
        T: FromStr,
        T::Err: Debug,
    {
        read_line_no_newline()
            .split_whitespace()
            .map(|t| t.parse::<T>().unwrap())
            .collect()
    }

    pub fn get_ints_n_lines<T>(n: usize) -> Vec<Vec<T>>
    where
        T: FromStr,
        T::Err: Debug,
    {
        (0..n).map(|_| get_ints::<T>()).collect()
    }

    pub fn get_string() -> String {
        read_line_no_newline()
    }

    pub fn get_string_n_lines(n: usize) -> Vec<String> {
        (0..n).map(|_| read_line_no_newline()).collect()
    }

    pub fn get_string_with_trim(sep: &str) -> Vec<String> {
        read_line_no_newline()
            .split(sep)
            .map(|x| x.to_string())
            .collect()
    }
}

#[derive(Default, Debug)]
struct Queue<T> {
    data: Vec<T>,
    pointer: usize,
}

impl<T: Copy> Queue<T> {
    fn dequeue(&mut self) -> Option<T> {
        if self.data.len() <= self.pointer {
            return None;
        }
        let v = self.data[self.pointer];
        self.pointer += 1;
        return Some(v);
    }

    fn enqueue(&mut self, v: T) {
        self.data.push(v);
    }

    fn peek(&self) -> Option<T> {
        if self.data.len() <= self.pointer {
            return None;
        }
        return Some(self.data[self.pointer]);
    }

    fn update(&mut self, v: T) {
        self.data[self.pointer] = v;
    }
}

enum Query {
    Enqueue(usize, usize),
    Dequeue(usize),
}

fn solve(queries: Vec<Query>) {
    let mut queue: Queue<(usize, usize)> = Queue::default();

    for q in queries {
        let mut sum = 0;
        match q {
            Query::Enqueue(c, x) => {
                queue.enqueue((c, x));
            }
            Query::Dequeue(mut k) => {
                while k > 0 {
                    let (c, x) = match queue.peek() {
                        Some(v) => (v.0, v.1),
                        None => break,
                    };

                    match c.cmp(&k) {
                        Ordering::Equal => {
                            sum += x * c;
                            queue.dequeue();
                        }
                        Ordering::Greater => {
                            sum += x * k;
                            queue.update((c - k, x));
                        }
                        Ordering::Less => {
                            sum += x * c;
                            queue.dequeue();
                        }
                    }
                    k = k.saturating_sub(c);
                }
                println!("{}", sum);
            }
        }
    }
}

fn main() {
    let q = io::get_int();
    let queries = get_ints_n_lines(q);

    let queries: Vec<Query> = queries
        .iter()
        .map(|query| {
            let query = match query[0] {
                1 => Query::Enqueue(query[1], query[2]),
                2 => Query::Dequeue(query[1]),
                _ => unreachable!(),
            };
            return query;
        })
        .collect();

    solve(queries);
}

// fn main() {
//     input! {
//         n: usize,
//         s: [String; n]
//     }

//     let mut set = HashSet::new();
//     for (i, left) in s.iter().enumerate() {
//         for (j, right) in s.iter().enumerate() {
//             if i == j {
//                 continue;
//             }
//             set.insert(format!("{left}{right}"));
//         }
//     }
//     println!("{}", set.len());
// }

// fn main() {
//     input! {
//         n: i32,
//         m: i32,
//         a: [i32; n]
//     }

//     if a.iter().sum::<i32>() <= m {
//         println!("Yes");
//     } else {
//         println!("No");
//     }
// }

// 絶対数に変換する
//
