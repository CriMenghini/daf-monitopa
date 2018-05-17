import React, { Component } from 'react';
import { VictoryBar, VictoryTooltip, VictoryAnimation, VictoryBrushLine, VictoryChart, VictoryLine, VictoryLabel, VictoryPie} from 'victory';
import PropTypes from 'prop-types';


class CustomLabel extends React.Component {
  render() {
    return (
      <g>
        <VictoryLabel {...this.props}/>
        <VictoryTooltip
          {...this.props}
          x={200} y={180}
          text={`${this.props.text}%`}
          orientation="top"
          pointerLength={0}
          cornerRadius={50}
          width={100}
          height={100}
          flyoutStyle={{ fill: "transparent" }}
        />
      </g>
    );
  }
}

CustomLabel.defaultEvents = VictoryTooltip.defaultEvents;
CustomLabel.propTypes = { text: PropTypes.string };

class Sentiment extends React.Component {
  render() {
    return (
        <VictoryPie  height={290}

          style={{ labels: { fontSize: 45,fill: (d) => d.y == this.props.sentiment[0].y ? "green":"red"}, data: {fill: (d) => { if (d.x == 1){return 'green'}
          else if (d.x == 2){return 'red'}
          else {return 'orange'};
              }}}}
          innerRadius={140}
          labelRadius={100}
          labels={(d) => d.y}//d.y >= 100 ? "green" : "red"
          labelComponent={<CustomLabel { ...this.props } { ...this.state}/>}
          data={this.props.sentiment}
        />
    );
  }
}

export default Sentiment;