function Student(marks1,marks2) {

    //Define and initialize both private properties here
    var _marks1 = marks1
    var _marks2 = marks2
  
  
    //Define the getMarks function on Student prototype here
    Student.prototype.getMarks = function(markNumber) {
      if(markNumber == 1)
        return _marks1
      else if(markNumber == 2)
        return _marks2
    }
    
    //Define the calcTotal function on Student prototype here
    Student.prototype.calcTotal = function() {
      // Write definition here
      this.totalMarks = _marks1 + _marks2
      return this.totalMarks
    }
}