#include "stdafx.h"


// Function definitions
float max(float n1, float n2);
float min(float n1,float n2);
float DistPoly(float x0,float y0, float xPol[300], float yPol[300], int nPol);
int InPoly(float x0,float y0, float xPol[300], float yPol[300], int nPol);


////////////////////////////////
///////// MAIN SECTION /////////
////////////////////////////////

int main(int argc, char* argv[])
{
	float PolyX[300];
	float PolyY[300];
	int NPoly = 8;

	PolyX[0] = 0;		PolyY[0] = 0;
	PolyX[1] = 1;		PolyY[1] = 2;
	PolyX[2] = 3;		PolyY[2] = 6;
	PolyX[3] = 2;		PolyY[3] = 8;
	PolyX[4] = 6;		PolyY[4] = 10;
	PolyX[5] = 9;		PolyY[5] = 5;
	PolyX[6] = 8;		PolyY[6] = 0;
	PolyX[7] = 4;		PolyY[7] = 2;
	PolyX[8] = 0;		PolyY[8] = 0;
	

	float X = 1;
	float Y = 1.73;
	cout << X << " " << Y << " " << DistPoly(X,Y,PolyX, PolyY, NPoly) << endl;
		
	return 0;
}



///////////////////////////////////////
//////////// FUNCTION DETAILS /////////
///////////////////////////////////////

float max(float n1, float n2)
{
	if (n1 > n2)
		return n1;
	else
		return n2;
};


float min(float n1,float n2)
{
	if (n1 > n2)
		return n2;
	else
		return n1;
}
	

// Program to determine the distance of a given point (x0,y0) from a given polygon.
// Polygon specified in terms of x and y co-ordinates, and number of vertives
// By definition, require xPol[nPol] == xPol[0] and yPol[nPol] == yPol[0]


float DistPoly(float x0,float y0, float xPol[300], float yPol[300], int nPol)
{
	float x1,x2,y1,y2;
	float S0,S1,S2,K;
	float MIN, Closest;
	int a;

	if ((nPol >= 300) || (xPol[nPol] != xPol[0]) | (xPol[nPol] != xPol[0]))
	{
		cout << "Illegal polygon specified" << endl;
		return -1;
	}
	
////////////////////////////////////////
///// See if point lies on an edge /////

	for (a=0; a < nPol; a++)
	{
		x1 = xPol[a];		y1 = yPol[a];
		x2 = xPol[a+1];		y2 = yPol[a+1];

		if ( (x1 == x2) && (x0 == x1) && (y0 <= max(x1,x2)) && (y0 >= min(x1,x2)) )
			return 0;
		if ( (y1 == y2) && (y0 == y1) && (x0 <= max(y1,y2)) && (x0 >= min(y1,y2)) )
			return 0;

		if (x1 != x2)
			if ( (y2-y1)/(x2-x1)*(x0-x1)+y1 == y0 )
				return 0;
	};
	

///// Find the sides, check the pythegorean relation to find if altitude falls within triangle

	MIN = float( sqrt( (x0-xPol[0])*(x0-xPol[0]) + (y0-yPol[0])*(y0-yPol[0]) ) );

	for (a=0; a < nPol; a++)
	{
		x1 = xPol[a];		y1 = yPol[a];
		x2 = xPol[a+1];		y2 = yPol[a+1];
        
        S0 = float(sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) ));
        S1 = float(sqrt( (x1-x0)*(x1-x0) + (y1-y0)*(y1-y0) ));       // Side lengths 
        S2 = float(sqrt( (x2-x0)*(x2-x0) + (y2-y0)*(y2-y0) ));
		K  = float(sqrt((S0+S1+S2)*(S0-S1+S2)*(S0+S1-S2)*(-S0+S1+S2))/4 );		
	
        if ( max(S1,S2)*max(S1,S2) > S0*S0 + S1*S1 + S2*S2 )		// Point of closest approach is a vertex
			Closest = min(S1,S2);
		else
			Closest = (2*K)/S0;
		
        if (MIN > Closest)
            MIN = Closest;
	
	};
	
	return MIN*InPoly(x0,y0,xPol,yPol,nPol);
};



/////////////////////////////////////////////////////////////////////////
// Function to see whether a given point lies inside specified polygon //
/////////////////////////////////////////////////////////////////////////


int InPoly(float x0,float y0, float xPol[300], float yPol[300], int nPol)
{
	bool NoProb;					// All is good (no ambiguity)
	int Inter;						// Number of intersections 
	float x1, x2, y1, y2, yCrit;
	
	x0 += 1e-9;
	do
	{
		x0 -= 1e-9;
		NoProb = true;
		Inter = 1;
		
		for (int a=0; a < nPol; a++)
		{
			x1 = xPol[a];		x2 = xPol[a+1];		
			y1 = yPol[a];		y2 = yPol[a+1];		

			if ((x1 == x2) && (x0 == x1))
				NoProb = false;

			if ((x0 <= max(x1,x2)) && (x0 > min(x1,x2)))
			{
				yCrit = (y2-y1)/(x2-x1)*(x0-x1)+y1;
				if (y0 > yCrit)
				{
					Inter *= -1;
				};
			};
		}
	}
	while (NoProb == false);	

	return Inter;

};