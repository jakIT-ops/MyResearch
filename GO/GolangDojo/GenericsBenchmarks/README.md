# Generics

## What's Generics?

Generics allows types to be parameters just like variables to functions 

## Performance?

One of the biggest hesitations (along with readability)

### Strategy 
    * Alternatives 
        * Type switch & type assertion
        ```
        i, ok := v.(int)
        f, ok := v.(float64)
        s, ok := v.(string)
        ```
        * Reflection & type assertion
        ```
        ok := reflect.TypeOf(v).Kind() == reflect.Int
        ok := reflect.TypeOf(v).Kind() == reflect.Float64
        ok := reflect.TypeOf(v).Kind() == reflect.String
        ```
        * Explicit
        ```
        func f(v int){}
        func f(v float64){}
        func f(v string){}
        ```

### Conclusion
    * Performance 
    ```
    254.4 ns/op BenchmarkAddExplicit
    254.8 ns/op BenchmarkAddGenerics
    254.9 ns/op BenchmarkAddGenericsWIthTypeSet
    259.9 ns/op BenchmarkAddTypeSwitch7
    511.4 ns/op BenchmarkAddReflection
    ```
