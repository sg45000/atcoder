{-# LANGUAGE TupleSections #-}

import Control.Monad (replicateM)
import Data.IntMap.Strict qualified as IntMap
import Data.IntSet qualified as IntSet
import Data.Maybe (fromJust)
import Data.Sequence (ViewL (..), ViewR (..), (><))
import Data.Sequence qualified as Seq

type Vertex = Int

type Graph = IntMap.IntMap [Vertex]

bfs graph vertex = bfs' (IntSet.singleton vertex) (Seq.singleton (vertex, 0))
 where
  bfs' visited queue = case Seq.viewl queue of
    EmptyL -> []
    x :< xs -> x : bfs' newVisited (xs >< Seq.fromList (map (,snd x + 1) newNeighbors))
     where
      neighbors = IntMap.findWithDefault [] (fst x) graph
      newNeighbors = filter (`IntSet.notMember` visited) neighbors
      newVisited = IntSet.union visited $ IntSet.fromList newNeighbors

dfs graph vertex = dfs' (IntSet.singleton vertex) (Seq.singleton vertex)
 where
  dfs' visited stack = case Seq.viewr stack of
    EmptyR -> []
    xs :> x -> x : dfs' newVisited (xs >< Seq.fromList newNeighbors)
     where
      neighbors = IntMap.findWithDefault [] x graph
      newNeighbors = filter (`IntSet.notMember` visited) neighbors
      newVisited = IntSet.union visited $ IntSet.fromList newNeighbors

main = do
  n <- readLn
  ab <- replicateM (n - 1) getLine
  let toGraph = map (\[a, b] -> (read a, [read b]))
  let graph = IntMap.fromListWith (++) $ toGraph (map words ab) ++ toGraph (map (reverse . words) ab)
  let dist1 = bfs graph 1
  let dist2 = bfs graph ((fst . last) dist1)
  print ((snd . last) dist2 + 1)