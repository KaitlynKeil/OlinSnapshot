
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
    var input_data =
      {
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
    //updateGraphics(input_data,quotes);
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
  //format data
  var nodes = pack.nodes(categories);

  //log some values to check
  console.log(5);
  console.log(quotes);
  console.log(categories);
  console.log(quotes.data[0].children);

  var node = chart.selectAll(".node")
      .data(nodes).enter()
      .append("g")
        .attr("class","node")
        .attr("transform",function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    //update old elements
    node.attr("class","update");

    //enter + update
    node.append("circle")
      .attr("class","enter")
      .attr("r",function(d) { return d.r })
      .attr("fill", function(d){ return d.children ? "#fff" : d.color; }) //make nodes with children invisible
      .attr("opacity", 0.25)
      .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
      .attr("stroke-width", 2);

    //add label with name information
    node.append("text")
      .text(function(d) {return d.children ? "" : d.name});

    //add click functionality
    node.on('click',datum => {
      console.log(datum);
      switch(datum.name){
        case "Food":
          var nodes = pack.nodes(quotes.data[0]);
          console.log("Food selected");
          console.log(nodes);
          break;
        case "Other":
          var nodes = pack.nodes(quotes.data[1]);
          console.log("Other selected");
          console.log(nodes);
          break;
        case "Events":
          var nodes = pack.nodes(quotes.data[2]);
          console.log("Events selected");
          console.log(nodes);
          break;
        case "Lost":
          var nodes = pack.nodes(quotes.data[3]);
          console.log("Lost selected");
          console.log(nodes);
          break;
        default:
          console.log("Category not found!")

      }
    });
    //remove old elements
    node.exit().remove();

    console.log("we tried!")

  });
};

/*var node = chart.selectAll(".node")
    .data(nodes).enter()
  .append("g")
    .attr("class", "node")
    .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

node.append("circle")
    .attr("r",function(d) { return d.r })
    .attr("fill", function(d){ return d.children ? "#fff" : d.color; }) //make nodes with children invisible
    .attr("opacity", 0.25)
    .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
    .attr("stroke-width", 2);

node.on('click',datum => {
      console.log(datum);
      update(datum.name);
    })

node.append("text")
    .text(function(d) { return d.children ? "" : d.name; });*/

//update reference d3 database object
function updateData(selected_category) {
  //choose correct data depending on selected_category
  switch(selected_category){
    case "Food":
      var nodes = pack.nodes(quotes.data[0]);
      console.log("did this update?????");
      console.log("Food selected");
      console.log(nodes);
      break;
    case "Other":
      var nodes = pack.nodes(quotes.data[1]);
      console.log("Other selected");
      console.log(nodes);
      break;
    case "Events":
      var nodes = pack.nodes(quotes.data[2]);
      console.log("Events selected");
      console.log(nodes);
      break;
    case "Lost":
      var nodes = pack.nodes(quotes.data[3]);
      console.log("Lost selected");
      console.log(nodes);
      break;
    default:
      console.log("Category not found!")

  }
};

function updateGraphics(input_data, quotes){
    //select all node and join new data in
    var node = chart.selectAll(".node")
      .data(input_data).enter()
      .append("g")
        .attr("class","node")
        .attr("transform",function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    //update old elements
    node.attr("class","update");

    //enter + update
    node.append("circle")
      .attr("class","enter")
      .attr("r",function(d) { return d.r })
      .attr("fill", function(d){ return d.children ? "#fff" : d.color; }) //make nodes with children invisible
      .attr("opacity", 0.25)
      .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
      .attr("stroke-width", 2);

    //add label with name information
    node.append("text")
      .text(function(d) {return d.children ? "" : d.name});

    //add click functionality
    node.on('click',datum => {
      console.log(datum);
      switch(datum.name){
        case "Food":
          var nodes = pack.nodes(quotes.data[0]);
          updateGraphics(nodes,quotes);
          console.log("Food selected");
          console.log(nodes);
          break;
        case "Other":
          var nodes = pack.nodes(quotes.data[1]);
          console.log("Other selected");
          updateGraphics(nodes,quotes);
          console.log(nodes);
          break;
        case "Events":
          var nodes = pack.nodes(quotes.data[2]);
          updateGraphics(nodes,quotes);
          console.log("Events selected");
          console.log(nodes);
          break;
        case "Lost":
          var nodes = pack.nodes(quotes.data[3]);
          updateGraphics(nodes,quotes);
          console.log("Lost selected");
          console.log(nodes);
          break;
        default:
          console.log("Category not found!")

      }
    });

    //remove old elements
    node.exit().remove();

    console.log("we tried!")
};
