# DevOps Model Defined

DevOps is the combination of cultural philosophies, practices, and tools that increases an organization's ability to deliver applications and services at high velocity

### Delivery Pipeline

BUILD > TEST > REALSE

< PLAN < MONITOR
# TinyGopackage main

import "errors"

func main() {
	f, err := someF()
	if err != nil {
		// Handle error...
		error
	}
	fmt.Println(f)
	f, err = someOtherF()
	if err != nil {
		// Handle error again...
		return
	}
	fmt.Println(f)
}

func someE() error {
	return errors.New("same type of error")
}


# Digital Ocean
