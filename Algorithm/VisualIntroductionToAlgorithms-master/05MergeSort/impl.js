// Takes in an array that has two sorted subarrays,
//  from [p..q] and [q+1..r], and merges the array
var merge = function(array, p, q, r) {
    // This code has been purposefully obfuscated,
    //  as you'll write it yourself in next challenge.
    var a=[],b=[],c=p,d,e;for(d=0;c<=q;d++,c++){a[d]=array[c];}for(e=0;c<=r;e++,c++){b[e]=array[c];}c=p;for(e=d=0;d<a.length&&e<b.length;){if(a[d]<b[e]){array[c]=a[d];d++;} else {array[c]=b[e]; e++;}c++; }for(;d<a.length;){array[c]=a[d];d++;c++;}for(;e<b.length;){array[c]=b[e];e++;c++;}
};


// Takes in an array and recursively merge sorts it
var mergeSort = function(array, p, r) {
  // Write this method
  
  
  
};
