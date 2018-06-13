import React, { Component } from 'react';
import { VictoryAxis, VictoryZoomContainer, VictoryBrushContainer,  VictoryArea, VictoryTheme, VictoryStack, VictoryBar, VictoryAnimation, VictoryBrushLine, VictoryChart, VictoryLine, VictoryLabel, VictoryPie} from 'victory';
//import { _ } from "jquery";
var _ = require('lodash');


class TimeSeries extends React.Component {
  constructor() {
    super();
    this.state = {
      zoomDomain: { x: [new Date(1990, 1, 1), new Date(2009, 1, 1)] }
    };
  }

  handleZoom(domain) {
    this.setState({ zoomDomain: domain });
  }


  parseDate(date) {
        var arrayDate = new Array();

        for (var i=0; i < date.length; i++){
            var dict = {a: new Date(date[i].a), b: date[i].b}
            arrayDate.push(dict)
        }
        return arrayDate
  }


  render() {
    return (
      <div>
        <VictoryChart width={600} height={270} scale={{ x: "time" }}
          containerComponent={
            <VictoryZoomContainer
              zoomDimension="x"
              zoomDomain={this.state.zoomDomain}
              onZoomDomainChange={this.handleZoom.bind(this)}
            />
          }
        >
            <VictoryLine animate={{ duration: 2000 }}
              style={{
                data: { stroke: "tomato" },
              }}
              data={this.parseDate(this.props.streamneg)}
              x="a"
              y="b"
            />
            <VictoryLine animate={{ duration: 2000 }}
              style={{
                data: { stroke: "green" },
              }}
              data={this.parseDate(this.props.streampos)}
              x="a"
              y="b"
            />
            <VictoryLine animate={{ duration: 2000 }}
              style={{
                data: { stroke: "orange"},
              }}
              data={this.parseDate(this.props.streamneu)}
              x="a"
              y="b"
            />

          </VictoryChart>
          <VictoryChart
            padding={{ top: 0, left: 50, right: 50, bottom: 30 }}
            width={600} height={100} scale={{ x: "time" }}
            containerComponent={
              <VictoryBrushContainer
                brushDimension="x"
                brushDomain={this.state.zoomDomain}
                onBrushDomainChange={this.handleZoom.bind(this)}
              />
            }
          >
            <VictoryAxis
              tickFormat={(x) => new Date(x).getFullYear()}
            />
            <VictoryLine
            animate={{ duration: 1000 }}
              style={{
                data: { stroke: "tomato" }
              }}
              data={this.parseDate(this.props.streamneg)}
              x="a"
              y="b"
            />
            <VictoryLine animate={{ duration: 1000 }}
              style={{
                data: { stroke: "green" },
              }}
              data={this.parseDate(this.props.streampos)}
              x="a"
              y="b"
            />
            <VictoryLine animate={{ duration: 1000 }}
              style={{
                data: { stroke: "orange" },
              }}
              data={this.parseDate(this.props.streamneu)}
              x="a"
              y="b"
            />
          </VictoryChart>
      </div>
    );
  }
}

export default TimeSeries;
