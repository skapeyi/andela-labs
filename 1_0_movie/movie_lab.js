function canIWatch(age){
	if(age % 1 == 0 && age >= 0){		
		if(age < 6){

			return 'You are not allowed to watch Deadpool after 6.00pm.';
		}
		else if( 6 <= age && age < 17){
			
			return 'You must be accompanied by a guardian who is 21 or older.';

		}
		else if( 17 <= age && age < 25){
			
			return 'You are allowed to watch Deadpool, right after you show some ID.' ;

		}
		else{
			
			return 'Yay! You can watch Deadpool with no strings attached!';
		}
	}
	else{
		
		return 'Invalid age.';
	}
}