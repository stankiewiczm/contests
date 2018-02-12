#include <stdio.h>
#include <iostream>
#include <cassert>

#include "bignum-nolib.cpp"

using namespace std;

int r = 43;
int s = 22;
long m = 1l<<32;

long long x[50];
long maxi = 42;
long long cprev = 0;

void initr()
{
	maxi = 42;
	cprev = 0;
}

long random()
{
	maxi++;
	long indnext = maxi % 50;
	long ind1 = (maxi - s) % 50;
	long ind2 = (maxi - r) % 50;
	long long val = x[ind1] - x[ind2] - cprev;

	cprev = (val < 0) ? 1 : 0;
	long long ans = val % m;
	if (ans < 0) {
		ans += m;
	}
	x[indnext] = ans;
	return (long) ans;
}

int main()
{
	for (long long i = 0; i <= 42; i++) {
		x[i] = (999999999ll * i * i * i) % m;
	}
	for (int i = 0; i < 3; i++) {
		cerr << "Testing random: " << random() << endl;
	}

	unsigned long long pows[64];
	Bignum bignums[100];
	pows[0] = 1;
	for (int i = 1; i < 64; i++) {
		pows[i] = pows[i - 1] * 2ll;
	}

	bignums[0] = Bignum(1);
	Bignum b2 = Bignum(2);
	for (int i = 1; i < 100; i++) {
		bignums[i] = bignums[i - 1] * b2;
	}

	int t;
	cin >> t;
	int maxval = 0;
	for (int caseNum = 1; caseNum <= t; caseNum++) {
		int n;
		cin >> n;
		long long strip[n];
		for (int i = 0; i < n; i++) {
			cin >> strip[i];
			if (strip[i] == 0) {
				strip[i] = -1;
			}
			else {
				bool found = false;
				for (int j = 0; j < 64; j++) {
					if (strip[i] == pows[j]) {
						strip[i] = j;
						found = true;
						break;
					}
				}
				assert(found);
			}
		}
		for (int i = 0; i < 43; i++) {
			cin >> x[i];
		}
		initr();

		int a;
		cin >> a >> ws;

		char dir;
		for (int move = 0; move < a; move++) {
			/*cerr << "    " << move << ": ";
			for (int i = 0; i < n; i++) {
				if (i > 0) {
					cerr << " ";
				}
				cerr << strip[i];
			}
			cerr << endl;*/
			cin >> dir;

			assert(dir == 'l' || dir == 'r');
			int d = dir == 'l' ? 1 : -1;

			int start = (dir == 'l') ? 0 : n - 1;
			int end = dir == 'l' ? n : -1;

			int cur = start;
			bool movemerge = false;
			int numempty = 0;
			int nonempty = -1;
			while (cur != end) {
				/*cerr << "s=" << start << "; e=" << end << "; c=" << cur << "; d=" << d << endl;
				cerr << "    " << move << ": ";
				for (int i = 0; i < n; i++) {
					if (i > 0) {
						cerr << " ";
					}
					cerr << strip[i];
				}
				cerr << endl;*/
				// If this block is empty, then try to shuffle in later blocks.
				if (strip[cur] == -1) {
					if (nonempty == -1) {
						nonempty = cur;
					}
					while (nonempty != end && strip[nonempty] == -1) {
						nonempty += d;
					}
					if (nonempty != end) {
						strip[cur] = strip[nonempty];
						strip[nonempty] = -1;
						movemerge = true;
					}
				}

				// Also try to shuffle in a block for the next cell.
				if (strip[cur] != -1 && cur + d != end && strip[cur + d] == -1) {
					if (nonempty == -1) {
						nonempty = cur + d;
					}
					while (nonempty != end && strip[nonempty] == -1) {
						nonempty += d;
					}
					if (nonempty != end) {
						strip[cur + d] = strip[nonempty];
						strip[nonempty] = -1;
						movemerge = true;
					}
				}

				// Now see if we can combine this block with the next one.
				if (strip[cur] != -1 && cur + d != end && strip[cur] == strip[cur + d]) {
					strip[cur] += 1;
					strip[cur + d] = -1;
					movemerge = true;
				}

				if (strip[cur] == -1) {
					numempty++;
				}

				cur += d;
			}

			if (movemerge) {
				// We moved or merged tiles, so randomly generate a new tile.
				int pos = random() % numempty;
				int newval = (random() % 10) == 0 ? 2 : 1;
				for (int cur = 0; cur < n; cur++) {
					if (strip[cur] == -1) {
						if (pos == 0) {
							strip[cur] = newval;
							break;
						}
						else {
							pos--;
						}
					}
				}
			}

			/*cerr << "    " << move << ": ";
			for (int i = 0; i < n; i++) {
				if (i > 0) {
					cerr << " ";
				}
				cerr << strip[i];
			}
			cerr << endl;*/
		}

		for (int i = 0; i < n; i++) {
			if (i > 0) {
				cout << " ";
			}
			if (strip[i] > maxval) {
				maxval = strip[i];
			}
			if (strip[i] >= 0) {
				cout << bignums[strip[i]];
			}
			else {
				cout << 0;
			}
		}
		cout << endl;
	}
	cerr << "max: " << maxval << endl;
}
