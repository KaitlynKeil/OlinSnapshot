var data_sample = [
    {"name":"Test1",
    "category": "Food",
    "location": "West Hall"
    },
    {"name":"Test2",
    "category": "Event",
    "location": "West Hall"
    },
    {"name":"Test3",
    "category": "Other",
    "location": "West Hall"
    },
    {"name":"Test4",
    "category": "Educational",
    "location": "West Hall"
    }
]
//Create the SVG body
var svg = d3.select("body")
    .append("svg")
    .attr("width", '800px')
    .attr("height", '800px');

//Create all the circle objects based on the data
svg.selectAll("circle")
    .data([32, 57, 112, 293]) //bind data
  .enter().append("circle") //create circles 
    .attr("cy", 60) //y axis
    .attr("cx", function(d, i) { return i * 100 + 30; }) //x axis
    .attr("r", function(d) { return Math.sqrt(d); }); //radius

//create an empty tool top
var tooltip = d3.select("body")
  .append ("div")
  .style("position", "absolute")
  .style("z-index", "10")
  .style("visibility", "hidden")
  .style("color", "white")
  .style("padding", "8px")
  .style("background-color", "rgba(0, 0, 0, 0.75)")
  .style("border-radius", "6px")
  .style("font", "12px sans-serif")
  .text("tooltip");
//
/*
createGraph();

function createGraph() {*/
    var width = 960; // chart width
    var height = 700; // chart height
    var format = d3.format(",d");  // convert value to integer
    //v3 syntax
    var color = d3.scale.category20();  // create ordinal scale with 20 colors
    var sizeOfRadius = d3.scale.pow().domain([-100,100]).range([-50,50]);  // https://github.com/mbostock/d3/wiki/Quantitative-Scales#pow

    //create bubble in a specific layout format
    var bubble = d3.layout.pack()
        .sort(null)  // disable sorting, use DOM tree traversal
        .size([width, height])  // chart layout size
        .padding(1)  // padding between circles
        .radius(function(d) { return 20 + (sizeOfRadius(d) * 30); });  // radius for each circle

    //initialize SVG Body/chart
    var svg = d3.select('#chart').append('svg') //add the bubbles to all charts
        .attr('width',width)
        .attr('height',height)
        .attr('class', 'bubble');

    //"LOAD" DATA
    var nodes = bubble.nodes(data_sample)
      
    //create a node for each bubble file
    var node = chart.selectAll(".node")
      //bind data 
      .data(nodes).enter()
    .append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    //add attributes to each create bubble
    node.append("circle")
      .attr("r",function(d) { return d.r; })
      .attr("fill", function(d){ return d.children ? "#fff" : "steelblue"; }) //make nodes with children invisible
      .attr("opacity", 0.25)
      .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
      .attr("stroke-width", 2);

    //add labeled text on top of each bubble
    node.append("text")
      .text(function(d) { return d.name; });


    
    //Load data, issue with referencing data.json while in local http server
/*    d3.json("/data/data.json", function(data) {
      //create data object
      var nodes = bubble.nodes(data_sample);
      
      //create a node for each bubble file
      var node = chart.selectAll(".node")
          //bind data 
          .data(nodes).enter()
        .append("g")
          .attr("class", "node")
          .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

      //add attributes to each create bubble
      node.append("circle")
          .attr("r",function(d) { return d.r; })
          .attr("fill", function(d){ return d.children ? "#fff" : "steelblue"; }) //make nodes with children invisible
          .attr("opacity", 0.25)
          .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
          .attr("stroke-width", 2);

      //add labeled text on top of each bubble
      node.append("text")
          .text(function(d) { return d.name; });
    });*/


//}

