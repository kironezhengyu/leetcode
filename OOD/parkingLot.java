/**
*
*  desgin a parking lot system
*  
* The parking lot has multiple levels. Each level has multiple rows of spots.
* The parking lot can park motorcycles, cars, and buses.
* The parking lot has motorcycle spots, compact spots, and large spots.
* A motorcycle can park in any spot.
* A car can park in either a single compact spot or a single large spot.
* A bus can park in five large spots that are consecutive and within the same row. 
* It cannot park in small spots.
**/


public enum Vehicles{
    Motorcycle,Compact,Large
}

public abstract class Vehicle {
    protected ArrayList<ParkingSpot> ParkingSpot = 
    new ArrayList<ParkingSpot>();
    protected String licencePlate;
    protected int spotNeed;
    protected VehicleSize size;

    public int getSpotNeeded(){
        return spotNeed;
    }
    public VehicleSize getSize(){
        return size;
    }
    public void setParking(int spots){
        ParkingSpot = spots;
    }
    public void clearSpots(){
        Q.revmoe();
        notifyAll();


    }

}


public class Bus extends Vehicles{

    public Bus(){
        spotNeed  = 5;
        size  = VehicleSize.LARGE;
    }
    // search for place to fit in 
    public boolean canFitIn():
}



public class Car extends Vehicles{

    public Car(){
        spotNeed = 1
        size = VehicleSize.Compact;
    }
    public boolean canFitIn();
}


/*
motocycle as well
**/

public class ParkingLot{
    private Level[] levels;
    private final int NUM_LEVELS = 5;

    public ParkingLot(){
        //constructor 
    }
    public boolean parkAvehicle(){
        notifyAll();
    }
}

public class Level{
    private int Floor;
    private ParkingSpot[] spots;
    private int AvailableSpots = 0;
    private static final int SPOT_PER_ROW =10;
    private Level(int flr, in numberSpots){
        //constructor
    }

    //setter and getter for avaliablespots
    public boolean parkAvehicle(){
        notifyAll();
    }
    public parkAtLevel(){
        this.avaliablespots --;
    }

    public remove(Vehicle veh){
        this.avaliablespots+veh.spotNeed;
        notifyAll();
    }
}

public ParkingSpot{

    private Vehicle veh;
    private int spotSize;
    private int position;
    private int spotNumber;
    private Level level;
    private boolean isAvalible;

    public ParkingSpot(Level lvl, int r, int n, Vehicle veh){
        ///
    }
    public isAvalible(){
        return this.isAvalible
    }
    public void removeCar(){
        ////
    }
}
/**
*head-head
*tail-head-head
*head-teail-head
*tai-tail-tail-head-head
**/




