# Interpolate
def lerp(a, b, t):
  return (1 - t) * a + t * b

# Inverse Interpolate
def inlerp(a, b, v):
  return ( v - a ) / ( b - a )

# Map
def map(a, b, c, d, v):
    return lerp(c, d, inlerp(a, b, v))

# Clamp
def clamp(a, b, v):
    return min(max(a, v), b)
