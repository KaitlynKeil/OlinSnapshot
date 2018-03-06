
//test kit
$(function() {
  console.log('jquery is working!');
  createGraph();
});

function createGraph() {
  // Code goes here
}


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
  var nodes = pack.nodes(quotes.data[0]);
  console.log(quotes);
  var node = chart.selectAll(".node")
      .data(nodes).enter()
    .append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  node.append("circle")
      .attr("r",function(d) { return d.r })
      .attr("fill", function(d){ return d.children ? "#fff" : "steelblue"; }) //make nodes with children invisible
      .attr("opacity", 0.25)
      .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
      .attr("stroke-width", 2);


  node.append("text")
      .text(function(d) { return d.children ? "" : d.name; });

});







