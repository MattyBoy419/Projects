package pet.java;

//Attributes
public class Dog {
private int dogSpaceNumber;
private double dogWeight;
private boolean grooming;

//Constructors for all attributes
public Dog (int dogSpaceNumber, double dogWeight, boolean grooming){
	this.dogSpaceNumber = dogSpaceNumber;
	this.dogWeight = dogWeight;
	this.grooming = grooming;
}

//Accessor(getter) for dogSpaceNumber
public int getDogSpaceNumber() {
	return dogSpaceNumber;
}

//Mutator(setter) for dogSpaceNumber
public void setDogSpaceNumber(int dogSpaceNumber) {
	this.dogSpaceNumber = dogSpaceNumber;
}

//Accessor(getter) for dogWeight
public double getDogWeight() {
	return dogWeight;
}

//Mutator(setter) for dogWeight
public void setDogWeight(double dogWeight) {
	this.dogWeight = dogWeight;
}

//Accessor(getter) for grooming
public boolean getGrooming() {
	return grooming;
}

//Mutator(setter) for grooming
public void setGrooming(boolean grooming) {
	this.grooming = grooming;
}	
}

