TRUE  = lambda a: lambda b: (a)
FALSE = lambda a: lambda b: (b)


(TRUE)(True)(False) == True
(FALSE)(True)(False) == False


AND   = lambda a: lambda b: (a)(b)(a)
OR    = lambda a: lambda b: (a)(a)(b)
NOT   = lambda a: lambda b: lambda c: (a)(c)(b)


(AND)(TRUE)(FALSE) == (FALSE)


(AND)(TRUE)(FALSE)(True)(False) == False


CONS = lambda a: lambda b: lambda c: (c)(a)(b)
CAR  = lambda a: (a)(TRUE)
CDR  = lambda a: (a)(FALSE)

(CAR)((CONS)(1)(2)) == 1
(CDR)((CONS)(1)(2)) == 2

UNCHURCH_BOOLEAN = (CONS)(True)(False)

(UNCHURCH_BOOLEAN)((NOT)(TRUE)) == False
(UNCHURCH_BOOLEAN)((OR)(TRUE)(FALSE)) == True

ZERO = FALSE
SUCC = lambda a: lambda b: lambda c: (b)((a)(b)(c))

ONE = (SUCC)(ZERO)
TWO = (SUCC)(ONE)
THREE = (SUCC)(TWO)
FOUR = (SUCC)(THREE)

def church_number(n):
    return SUCC(church_number(n - 1)) if n else FALSE

PLUS = lambda a: lambda b: lambda c: lambda d: (a)(c)((b)(c)(d))
MULT = lambda a: lambda b: lambda c: (b)((a)(c))
EXP  = lambda a: lambda b: (b)(a)

UNCHURCH_NUMBER = lambda a: (a)(lambda b: b + 1)(0)

(UNCHURCH_NUMBER)(ZERO) == 0
(UNCHURCH_NUMBER)(ONE) == 1
(UNCHURCH_NUMBER)(TWO) == 2

(UNCHURCH_NUMBER)((PLUS)(THREE)(TWO)) == 5
(UNCHURCH_NUMBER)((MULT)(THREE)(TWO)) == 6
(UNCHURCH_NUMBER)((EXP)(THREE)(TWO)) == 9
