package io.datajek.unittesting;

public class ArrayMethods {

	int findIndex(int[] array, int number) {
		int index = -1;
		for(int i=0; i<array.length; i++){
			if(array[i]==number)
				index=i;
		}
		return index;
	}
	
	boolean searchForNumber(int[] array, int numberToSearchFor) {  //search for number, return true if found
		boolean found = false;
		for(int i:array) {
			if(array[i]== numberToSearchFor) {
				found = true;
				return found;
			}
		}
		return found;
	}
}
