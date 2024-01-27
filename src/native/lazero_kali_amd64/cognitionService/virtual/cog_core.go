package main

import . "fmt"
import . "strings"
import R "reflect"

func main(){
	Println(Contains("animalsfood", "foo"))

	// 'bar' does not present in 'birdsfood'
	Println(Contains("birdsfood", "bar"))

	Println(Contains("animalsfood", ""))

	Println(Contains("", ""))
	Println(R.TypeOf(R.TypeOf))
	Println(R.TypeOf(R.TypeOf).Kind())
	//Println(R.TypeOf(R.TypeOf).Kind().Field())
	// go doc reflect
}
