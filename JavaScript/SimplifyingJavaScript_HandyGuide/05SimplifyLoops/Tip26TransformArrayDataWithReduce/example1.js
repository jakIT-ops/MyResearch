const dogs = [{
		name: 'max',
		size: 'small',
		breed: 'boston terrier',
		color: 'black',
	},
	{
		name: 'don',
		size: 'large',
		breed: 'labrador',
		color: 'black',
	},
	{
		name: 'shadow',
		size: 'medium',
		breed: 'labrador',
		color: 'chocolate',
	},
];

const filters = dogs.reduce((filters, item) => {
	filters.breed.add(item.breed);
	filters.size.add(item.size);
	filters.color.add(item.color);
	return filters;
}, {
	breed: new Set(),
	size: new Set(),
	color: new Set(),
});

console.log(filters);
