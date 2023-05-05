data Relation = Inside | InsideTouch | Overlap | OutsideTouch | Outside
data Point = Point Int Int

type Radius = Int
data Circle = Circle Point Radius

relation (Circle (Point x1 y1) r1) (Circle (Point x2 y2) r2)
  | (r1 + r2) ^ 2 < centerDistanceSquared = Outside
  | (r1 + r2) ^ 2 == centerDistanceSquared = OutsideTouch
  | (r1 - r2) ^ 2 < centerDistanceSquared && centerDistanceSquared < (r1 + r2) ^ 2 = Overlap
  | (r1 - r2) ^ 2 == centerDistanceSquared = InsideTouch
  | (r1 - r2) ^ 2 > centerDistanceSquared = Inside
 where
  centerDistanceSquared = pow (x1 - x2) + pow (y1 - y2)
  pow x = x * x
