#include <iostream>
#include <set>

void runProgram()
{
	// init
	int programCounter = 0;
	long a=1,b=0,c=0,d=0,e=0,f=0,g=0,h=0;
	int numMulCalls = 0;
	long numIterations = 0;

	// run
	while(programCounter >= 0 && programCounter < 32)
	{
		numIterations++;
		switch(programCounter)
		{
			case 0:
				//set b 99
				// std::cout << "set b 99" << std::endl;
				b = 99;
				programCounter++;
				break;
			case 1:
				//set c b
				// std::cout << "set c b" << std::endl;
				c = b;
				programCounter++;
				break;
			case 2:
				//jnz a 2
				// std::cout << "jnz a 2" << std::endl;
				if(a != 0)
					programCounter+=2;
				else	
					programCounter++;
				break;
			case 3:
				//jnz 1 5 = TRUE!
				// std::cout << "jnz 1 5" << std::endl;
				programCounter+=5;
				break;
			case 4:
				//mul b 100
				// std::cout << "mul b 100" << std::endl;
				numMulCalls++;
				b *= 100;
				programCounter++;
				break;
			case 5:
				//sub b -100000
				// std::cout << "sub b -100000" << std::endl;
				b += 100000;
				programCounter++;
				break;
			case 6:
				//set c b
				// std::cout << "set c b" << std::endl;
				c = b;
				programCounter++;
				break;
			case 7:
				//sub c -17000
				// std::cout << "sub c -17000" << std::endl;
				c += 17000;
				programCounter++;
				break;
			case 8:
				//set f 1
				// std::cout << "set f 1" << std::endl;
				f = 1;
				programCounter++;
				break;
			case 9:
				//set d 2
				// std::cout << "set d 2" << std::endl;
				d = 2;
				programCounter++;
				break;
			case 10:
				//set e 2
				// std::cout << "set e 2" << std::endl;
				e = 2;
				programCounter++;
				break;
			case 11:
				//set g d
				// std::cout << "set g d" << std::endl;
				g = d;
				programCounter++;
				break;
			case 12:
				//mul g e
				// std::cout << "mul g e" << std::endl;
				g *= e;
				numMulCalls++;
				programCounter++;
				break;
			case 13:
				//sub g b
				// std::cout << "sub g b" << std::endl;
				g -= b;
				programCounter++;
				break;
			case 14:
				//jnz g 2
				// std::cout << "jnz g 2" << std::endl;
				if(g != 0)
					programCounter+=2;
				else	
					programCounter++;
				break;
			case 15:
				//set f 0
				// std::cout << "set f 0" << std::endl;
				f = 0;
				programCounter++;
				break;
			case 16:
				//sub e -1
				// std::cout << "sub e -1" << std::endl;
				e++;
				programCounter++;
				break;
			case 17:
				//set g e
				// std::cout << "set g e" << std::endl;
				g = e;
				programCounter++;
				break;
			case 18:
				//sub g b
				// std::cout << "sub g b" << std::endl;
				g -= b;
				programCounter++;
				break;
			case 19:
				//jnz g -8
				// std::cout << "jnz g -8" << std::endl;
				if(g != 0)
					programCounter-=8;
				else	
					programCounter++;
				break;
			case 20:
				//sub d -1
				// std::cout << "sub d -1" << std::endl;
				d++;
				programCounter++;
				break;
			case 21:
				//set g d
				// std::cout << "set g d" << std::endl;
				g = d;
				programCounter++;
				break;
			case 22:
				//sub g b
				// std::cout << "sub g b" << std::endl;
				g -= b;
				programCounter++;
				break;
			case 23:
				//jnz g -13
				// std::cout << "jnz g -13" << std::endl;
				if(g != 0)
					programCounter-=13;
				else	
					programCounter++;
				break;
			case 24:
				//jnz f 2
				// std::cout << "jnz f 2" << std::endl;
				if(f != 0)
					programCounter+=2;
				else	
					programCounter++;
				break;
			case 25:
				//sub h -1
				// std::cout << "sub h -1" << std::endl;
				h++;
				programCounter++;
				break;
			case 26:
				//set g b
				// std::cout << "set g b" << std::endl;
				g = b;
				programCounter++;
				break;
			case 27:
				//sub g c
				// std::cout << "sub g c" << std::endl;
				g -= c;
				programCounter++;
				break;
			case 28:
				//jnz g 2
				// std::cout << "jnz g 2" << std::endl;
				if(g != 0)
					programCounter+=2;
				else	
					programCounter++;
				break;
			case 29:
				//jnz 1 3 = TRUE
				// std::cout << "jnz 1 3" << std::endl;
				programCounter+=3;
				break;
			case 30:
				//sub b -17
				// std::cout << "sub b -17" << std::endl;
				b += 17;
				programCounter++;
				break;
			case 31:
				//jnz 1 -23 = TRUE!
				// std::cout << "jnz 1 -23" << std::endl;
				programCounter-=23;
				break;
		} // switch

		if(numIterations % 10000 == 0)
		{
			std::cout << "After step " << numIterations << ", programCounter at " << programCounter << ":" 
				  << "\ta = " << a
				  << "\t\tb = " << b
				  << "\t\tc = " << c
				  << "\t\td = " << d
				  << "\t\te = " << e
				  << "\t\tf = " << f
				  << "\t\tg = " << g
				  << "\t\th = " << h << std::endl;
		}
	} // while
	std::cout << "Finished after " << numIterations << " iterations and mul called " << numMulCalls << " times" << std::endl;
	std::cout << "After step " << numIterations << ", programCounter at " << programCounter << ":" 
				  << "\ta = " << a
				  << "\t\tb = " << b
				  << "\t\tc = " << c
				  << "\t\td = " << d
				  << "\t\te = " << e
				  << "\t\tf = " << f
				  << "\t\tg = " << g
				  << "\t\th = " << h << std::endl;
}


void runOptimizedProgram()
{
	// long b = 109900;
	long b = 108400;
	long c = b + 17000;
	long h = 0;
	long prod = 0;

	std::set<long> foundNumbers;

	for(long d = 2; d < c; d++)
	{
		for(long e = 2; e < c; e++)
		{
			prod = d*e;
			if(prod >= b && prod <= c && (prod - b) % 17 == 0)
			{
				foundNumbers.insert(prod);
			}
		}
	}

	std::cout << "Found " << foundNumbers.size() << " numbers that are a product of two numbers from the given range" << std::endl;
}

int main() {
	// runProgram();
	runOptimizedProgram();
	return 0;
}