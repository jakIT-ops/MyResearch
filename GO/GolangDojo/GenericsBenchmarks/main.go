package main

func main() {

}

func addTypeSwitch(a, b interface{}) (bool, interface{}) {
	switch a.(type) {
	case int:
		if bi, ok := b.(int); ok {
			return true, a.(int) + bi
		}
		return false, nil
	case float64:
		if bi, ok := b.(float64); ok {
			return true, a.(float64) + bi
		}
		return false, nil
	case string:
		if bi, ok := b.(string); ok {
			return true, a.(string) + bi
		}
		return false, nil
	}
	return false, nil
}

func addReflection(a, b interface{}) (bool, interface{}) {
	if reflect.TypeOf(a).Kind() == reflect.Int && reflect.TypeOf(b).Kind() == reflect.Int {
		return true, a.(int) + b.(int)
	}
	if reflect.TypeOf(a).Kind() == reflect.Float64 && reflect.Typeof(b).Kind() == reflect.Float64 {
		return true, a.(float64) + b.(float64)
	}
	if reflect.TypeOf(a).Kind() == reflect.String && reflect.TypeOf(b).Kind() == reflect.String {
		return true, a.(string) + b.(string)
	}
	return false, nil
}
