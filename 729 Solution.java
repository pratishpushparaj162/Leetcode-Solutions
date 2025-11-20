// class MyCalendar {

//     public MyCalendar() {
        
//     }
    
//     public boolean book(int startTime, int endTime) {
        
//     }
// }

//Basic model to represent a booking duration only
class Duration {
	private int start;
	private int end;

	public Duration(int start, int end) {
		this.start = start;
		this.end = end;
	}
	//Getters to access start and end times
	public int getStart() {
		return start;
	}
	public int getEnd() {
		return end;
	}
}

public class MyCalendar {
	//Container to hold all existing bookings
	private List<Duration> bookings = new ArrayList<>();

    public MyCalendar() {}
    
    public boolean book(int startTime, int endTime) {
    	//If there are no existing bookings, add the new booking directly
        if (bookings.isEmpty()) {
			bookings.add(new Duration(startTime, endTime));
			return true;
			
		} else {
				//Compare all existing bookings for overlap with the new booking proposal
				for (Duration duration : bookings) {
					//Check to see if there is an overlap
					if (startTime < duration.getEnd() && endTime > duration.getStart()) {
						return false; // overlap found, booking cannot be made
					}
				}
			
			//Overlap not found, add the new booking
			bookings.add(new Duration(startTime, endTime));
			
			return true;
		}
    }
}
