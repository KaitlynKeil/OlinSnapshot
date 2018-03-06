
//test kit
$(function() {
  console.log('jquery is working!');
  createGraph();
});

function createGraph() {
  //set screen pixel sizes
  var width = 800, height = 600;

  //set up the image chart
  var chart = d3.select("body").append("svg")
    .attr("width", width).attr("height", height) 
    .append("g")
      .attr("transform", "translate(50,50)");

  //identify what layout package we're taking from d3
  var pack = d3.layout.pack()
    .size([width, height - 50])
    .padding(10);

  //Requesting the data bound to /data endpoint
  d3.json("/data", function(error,quotes) {
    //bind data 
    var nodes = pack.nodes(quotes.data[0]);
    //create category json 
    var categories = {
    "name": "Categories",
    "value": 60,
    "children": [
      {
        "name":  "Food",
        "value": quotes.data[0].children.length * 5,
        "color": "green"
      },
      {
        "name":  "Other",
        "value": quotes.data[1].children.length * 5,
        "color": "purple"
      },
      {
        "name":  "Lost",
        "value": quotes.data[2].children.length * 5,
        "color": "red"
      },
      {
        "name":  "Events",
        "value": quotes.data[3].children.length * 5,
        "color": "blue"
      }
    ]
  };
  //log some values to check
  console.log(5);
  console.log(quotes);
  //bind data
  var node = chart.selectAll(".node")
      .data(categories).enter()
    .append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  // set properties based on the data
  node.append("circle")
      .attr("r",function(d) { return d.r })
      .attr("fill", function(d){ return d.children ? "#fff" : "steelblue"; }) //make nodes with children invisible
      .attr("opacity", 0.25)
      .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
      .attr("stroke-width", 2);

  // add category labels
  node.append("text")
      .text(function(d) { return d.children ? "" : d.name; });

  });
};













