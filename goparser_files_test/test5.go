func gcd(a int, b int) int {

	if b == 0 {
		return a;
	}

	return gcd(b,a%b);
}

print gcd(3178, 252);
