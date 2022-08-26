const keyValueArray = [
  ['key1', 'value1'],
  ['key2', 'value2']
]

const obj = Object.fromEntries(keyValueArray);
console.log(obj);
// {key1: "value1", key2: "value2"}
