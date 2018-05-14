import React, { Component } from 'react';
import { VictoryBar, VictoryAnimation, VictoryBrushLine, VictoryChart, VictoryLine, VictoryLabel, VictoryPie} from 'victory';

class NumTweet extends React.Component {
  constructor() {
    super();
    this.state = {
      percent: 0, data: this.getData(0)
    };
  }


  componentDidMount() {
    let percent = 0;
    this.setStateInterval = window.setInterval(() => {
      percent += 10;
      if (percent >= 101)
        {this.myStopFunction()}

      else{this.setState({
        percent, data: this.getData(percent)
      })};
    }, 2000);
  }

  componentWillUnmount() {
    window.clearInterval(this.setStateInterval);
  }

  getData(percent) {
    return [{ x: 1, y: percent }, { x: 2, y: 100 - percent }];
  }

  myStopFunction() {
    clearInterval(this.setStateInterval);
    }

  render() {
    return (
      <div>
        <svg viewBox="0 0 400 400" width="100%" height="100%">
          <VictoryPie
            standalone={false}
            animate={{ duration: 1000 }}
            width={400} height={300}
            data={this.state.data}
            innerRadius={120}
            cornerRadius={25}
            labels={() => null}
            style={{
              data: { fill: (d) => {
                const color = d.y >= 100 ? "green" : "red";
                return d.x === 1 ? color : "grey";
              }
              }
            }}
          />
          <VictoryAnimation duration={1000} data={this.state}>
            {(newProps) => {
              return (
                <VictoryLabel
                  textAnchor="middle" verticalAnchor="middle"
                  x={200} y={150}
                  text={`${Math.round(newProps.percent)}`}
                  style={{ fontSize: 45 }}
                />
              );
            }}
          </VictoryAnimation>
        </svg>
      </div>
    );
  }
}

export default NumTweet;