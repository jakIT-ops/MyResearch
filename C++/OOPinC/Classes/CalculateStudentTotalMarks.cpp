class Student
{
    private:
       float mark1;
       float mark2;
       string name;

    public:
       // Constructor with no arguments (default constructor)
       Student() {
         name = "";
         mark1=0;
         mark2=0;
       }

       // Constructor with three arguments
       Student(string na, float ma1,float ma2) {
         name=na;
         mark1=ma1;
         mark2=ma2;
       }

       int GetMarks(int marknumber) {
           if(marknumber == 1){
             return mark1;
           }
           else{
             return mark2;
           }
       }

       float calc_total() {
         return (mark1+mark2);
       }
};





