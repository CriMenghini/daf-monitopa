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
          x={200} y={170}
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
    return (<div>
        <br />
        <VictoryPie  height={250}

          style={{ labels: { fontSize: 30,fill: (d) =>  {if (d.x == 1){return 'green'}
                                                         else if (d.x == 2){return 'red'}
                                                         else {return 'orange'};}  },
                   data: { fill: (d) => { if (d.x == 1){return 'green'}
                                          else if (d.x == 2){return 'red'}
                                          else {return 'orange'};
                                              }}}}
          innerRadius={110}
          labelRadius={300}
          labels={(d) => d.y}//d.y >= 100 ? "green" : "red"
          labelComponent={<CustomLabel { ...this.props } { ...this.state}/>}
          data={this.props.sentiment}
        />
        </div>
    );
  }
}

export default Sentiment;