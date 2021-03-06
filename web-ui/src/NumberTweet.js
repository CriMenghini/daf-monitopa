import React, { Component } from 'react';
import { VictoryBar, VictoryAnimation, VictoryBrushLine, VictoryChart, VictoryLine, VictoryLabel, VictoryPie} from 'victory';



class NumTweet extends React.Component {
  constructor() {
    super();
    this.state = {
      dati: this.getData(0),
      percent: 0
    };
  }


  componentDidMount() {
    let percent = 0;
    this.setStateInterval = window.setInterval(() => {
      percent += this.props.numtweet/3;
      if (percent >= this.props.numtweet+1)
        {this.myStopFunction()}

      else{this.setState({
        percent, dati: this.getData(percent)
      })};
    }, 2000);
  }

  componentWillUnmount() {
    window.clearInterval(this.setStateInterval);
  }

  getData(percent) {
    return [{ x: 1, y: percent }, { x: 1, y: 100 - percent }];
  }

  myStopFunction() {
    clearInterval(this.setStateInterval);
    }



  render() {
    return (
      <div>
        <svg viewBox="-50 -40 500 350" width="100%" height="100%" id='svgprova'>
          <VictoryPie
            standalone={false}
            animate={{ duration: 1000 }}
            width={400} height={300}
            data={[{x: 2, y: this.props.numtweet}]}
            innerRadius={120}
            cornerRadius={25}
            labels={() => null}
            style={{
              data: { fill: (d) => {
                const color = d.y >= 100 ? "red" : "green";
                return d.x === 1 ? color : "green";
              }
              }
            }}
          />
          <VictoryAnimation duration={1000} data={{dati: [{x: 1, y: this.props.numtweet}, {x:2, y:1000-this.props.numtweet}], percent: this.state.percent}}>
            {(newProps) => {
              return (
                <VictoryLabel
                  textAnchor="middle" verticalAnchor="middle"
                  x={200} y={150}
                  text={`${Math.round(this.props.numtweet)}`}
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