function addClick(items) {
	for (let i = 0; i < items.length; i++) {
		items[i].onClick = function () { return i; };
	}
	return items;
}
const example = [{}, {}];
const clickSet = addClick(example);
console.log(clickSet[0].onClick());
