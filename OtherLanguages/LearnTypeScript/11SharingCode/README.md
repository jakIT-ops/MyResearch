# 1. Namespace

### Namespace: A fading concept

The concept of namespaces in TypeScript is fading away with the second, more powerful way to share code: a module. A namespace is a basic object assigned to the global space. The object, named after the name of the namespace, holds the functions created within this one.

### Goal of using a namespace

```ts
namespace namespace1 {
    export let variable_ns1: number = 1;
}

namespace namespace1 {
    export let variable_ns1_also: number = 2;
}

namespace namespace2 {
    export let variable_ns2: number = 3;
}

console.log(namespace1.variable_ns1);
console.log(namespace1.variable_ns1_also);
console.log(namespace2.variable_ns2);
```

# 2. Module

### Separation of the module

```ts
export const module1_variable1 = "test"; 
export interface module1_interface1 { m1: string; } 
```

```ts
export * from "./module1"; 
```

```ts
import { module1_variable1, module1_interface1 } from "./module1"; 
import * as EverythingFromModule1 from "./module1"; 

console.log(module1_variable1); 
console.log(EverythingFromModule1.module1_variable1); 
```

# 3. Default Module

### Module with default export

```ts
//One file named "module4.ts" 
interface module4Interface { m1: string } 
export default module4Interface; 
 
// Another file 
import Def from "./module4"; 
const defModule4: Def = { m1: "A string" }
```

```ts
export default (input: number) => input * 10; 
```

### Avoiding default module

```ts
// Module1.ts
export default function () {console.log("function");}

// Import in file1.ts
import nameABC from "./Module1"

// Import in file1.ts
import nameXYZ from "./Module1"
```

# 4. Lazy Loading Module

TypeScript analyzes the code while transpiling into JavaScript and can detect if an import is being used only for its type or not. Removing code is an important notion which helps to remove the size of the bundle of dependencies. It is also important if you want to lazy load a module. Lazy loading is the principle of loading on-demand when the module is required. Lazy loading gives a performance boost by initially only loading what is needed. Hereafter, the lazy loading pattern can load additional modules for a particular route or for particular actions. The support for lazy loading is still in an infantile stage with a syntax that requires being closer to a specific module target.

```ts
import module1_variable1 = require("./module1"); 
export function lazyLoadWhenInvoked() {     
  const _foo: typeof module1_variable1 = require("./module1");   
  console.log(_foo.module1_variable1); 
} 
lazyLoadWhenInvoked(); 
```

```ts
async function getVariableLazyLoaded1(): Promise<string> {     
  const mod1 = await import("./module1");     
  const varFromOtherModule = await mod1.module1_variable1;     
    return Promise.resolve(varFromOtherModule); 
}
```

```ts
function getVariableLazyLoaded2(): Promise<string> {     
    return import("./module1").then(mod1 => {         
        return mod1.module1_variable1;     
    }); 
  } 
```

```ts
return import(/* webpackChunkName: "bundleAbc" */"./module1").then(…); 
```


