const draw = (x, y, color) =>{
    fetch("http://192.168.1.41:5000/set/", {
        method: "POST",
        body: JSON.stringify({
            "x": x,
            "y": y,
            "color": color,
        }),
        headers: {
            "Content-type": "application/json",
        }
    })
}