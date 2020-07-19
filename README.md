# Premise
allows for code golfing recurrence relations easy, uses maths stuff -> 2 things next to each other multiply etc

# Things
- n ->input
- b-d -> a(n-1) - a(n-3)
- A-D -> n - n-3
- n! -> n factorial
- numbers -> literal
- numbers at end -> seed data (if not enough values eg. 1 value but features n-2, duplicate)
- </> -> increment/decrement
- ) -> end section else first thing
- ' -> concat
- < > = -> comparison (less, greater, equal to) right side is always number, expression or defined set (if equal) count n up until true
- i -> iterator (to be used with comparison)

## Sets
- {s -> sqaures
- {p -> primes
- {f -> fibonacci

# Examples
## Working

| program name | mathematical definition | code | python function generated |
| ------------ | -- | -- | -- |
| Factorial (non builtin) | f(n)=n\*f(n-1), f(0)=1 | `nb1` | f=lambda n:n>1 and n*f(n-1)or 1 |
| Telephone numbers | T(n)=T(n-1)+(n-1)T(n-2), f(0)=1, f(1)=1 | `b+Bc1` | T=lambda n:1 if n<2 else T(n-1)+(n-1)*T(n-2) |
| Sum of first `n` natural numbers | sum(n)=n+sum(n-1) if n > 0 | `n+b1` | f=lambda n: n+f(n-1) if n > 1 else 1 |


## Not working (yet)
| program name | mathematical definition | code | python function generated |
| ------------ | -- | -- | -- |
| Fibonacci | f(n)=f(n-1)+f(n-2), f(0)=1 f(1)=1 | a+b01 | f=lambda n:n if n<2 else f(n-1)+f(n-2) |
| A071176 | | n'i=s | f=lambda n, k=0:k if 'n'+'k' in sqaures else f(n,k+1) |

# Contributing
If you would like to submit any ideas or whatever just add an issue. The implementation is really poor and hacky at the moment. I will change that if I can be bothered or someone else can do it if they wnat.