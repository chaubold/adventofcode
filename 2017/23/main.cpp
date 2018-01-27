#include <iostream>

enum RegisterIndex
{
	a = 0,
	b,
	c,
	d,
	e,
	f,
	g,
	h,
	NUM_REGISTERS
};

void runProgram()
{
	// init
	int programCounter = 0;
	int registers[NUM_REGISTERS];
	for(int i = 0; i < NUM_REGISTERS; i++)
	{
		registers[i] = 0;
	}
	int numMulCalls = 0;
	int numIterations = 0;

	// run
	while(programCounter >= 0 && programCounter < 32)
	{
		numIterations++;
		switch(programCounter)
		{
			case 0:
				//set b 99
				registers[b] = 99;
				programCounter++;
				break;
			case 1:
				//set c b
				registers[c] = registers[b];
				programCounter++;
				break;
			case 2:
				//jnz a 2
				if(registers[a] == 0)
					programCounter+=2;
				else	
					programCounter++;
				break;
			case 3:
				//jnz 1 5 = FALSE
				programCounter++;
				break;
			case 4:
				//mul b 100
				numMulCalls++;
				programCounter++;
				break;
			case 5:
				//sub b -100000
				programCounter++;
				break;
			case 6:
				//set c b
				programCounter++;
				break;
			case 7:
				//sub c -17000
				programCounter++;
				break;
			case 8:
				//set f 1
				programCounter++;
				break;
			case 9:
				//set d 2
				programCounter++;
				break;
			case 10:
				//set e 2
				programCounter++;
				break;
			case 11:
				//set g d
				programCounter++;
				break;
			case 12:
				//mul g e
				programCounter++;
				break;
			case 13:
				//sub g b
				programCounter++;
				break;
			case 14:
				//jnz g 2
				if(registers[g] == 0)
					programCounter+=2;
				else	
					programCounter++;
				break;
			case 15:
				//set f 0
				programCounter++;
				break;
			case 16:
				//sub e -1
				programCounter++;
				break;
			case 17:
				//set g e
				programCounter++;
				break;
			case 18:
				//sub g b
				programCounter++;
				break;
			case 19:
				//jnz g -8
				if(registers[g] == 0)
					programCounter-=8;
				else	
					programCounter++;
				break;
			case 20:
				//sub d -1
				programCounter++;
				break;
			case 21:
				//set g d
				programCounter++;
				break;
			case 22:
				//sub g b
				programCounter++;
				break;
			case 23:
				//jnz g -13
				if(registers[g] == 0)
					programCounter-=13;
				else	
					programCounter++;
				break;
			case 24:
				//jnz f 2
				if(registers[f] == 0)
					programCounter+=2;
				else	
					programCounter++;
				break;
			case 25:
				//sub h -1
				programCounter++;
				break;
			case 26:
				//set g b
				programCounter++;
				break;
			case 27:
				//sub g c
				programCounter++;
				break;
			case 28:
				//jnz g 2
				if(registers[g] == 0)
					programCounter+=2;
				else	
					programCounter++;
				break;
			case 29:
				//jnz 1 3 = FALSE!
				programCounter++;
				break;
			case 30:
				//sub b -17
				programCounter++;
				break;
			case 31:
				//jnz 1 -23 = FALSE!
				programCounter++;
				break;
		}
	}
}


int main() {
	runProgram();
	return 0;
}