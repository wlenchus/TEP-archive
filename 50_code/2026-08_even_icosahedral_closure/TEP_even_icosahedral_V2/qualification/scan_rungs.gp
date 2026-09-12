{
print("1951 prime: ", isprime(1951), "  1951%4=", 1951%4, "  1951%5=", 1951%5, "  primroot=", lift(znprimroot(1951)));
print("bigD 3806549: prime=", isprime(3806549), " fundamental=", isfundamental(3806549), " h=", quadclassunit(3806549).no);
print("matched scan (D prime, D=1 mod 4, h=3, D in [1902,2600]):");
forprime(D=1902,2600, if(D%4==1 && quadclassunit(D).no==3, print("  D=",D," h=3")));
print("mid scan (D prime, D=1 mod 4, h=3, D in [39900,41500]):");
forprime(D=39900,41500, if(D%4==1 && quadclassunit(D).no==3, print("  D=",D," h=3")));
}
quit
