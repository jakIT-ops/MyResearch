const landscape = {
    title: 'Landscape',
    photographer: 'Nathan',
    location: [32.7122222, -103.1405556],
};

function determineCityAndState([latitude, longitude]) {
    // Geo lookup would happen here
    const region = {
        city: 'Hobbs',
        county: 'Lea',
        state: {
            name: 'New Mexico',
            abbreviation: 'NM',
        },
    };
    return region;
}

function setRegion({ location, ...details }) {
    const { city, state } = determineCityAndState(location);
    return {
        city,
        state: state.abbreviation,
        ...details,
    };
}

console.log(setRegion(landscape));
