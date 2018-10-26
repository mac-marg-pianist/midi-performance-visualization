import React, { Component } from 'react';
import { Stage, Layer, Rect, Text } from 'react-konva';
import Konva from 'konva';

function value_limit(val, min, max) {
  return val < min ? min : (val > max ? max : val);
}

class Scroll extends Component {
  static defaultProps = {
    setTime: () =>  console.warn('setTime not defined'),
  };

  state = {
    scroll_size: window.innerWidth - 13*2,
    percentage: 0
  };

  componentDidMount() {
    window.addEventListener("resize", this.resize.bind(this));
    this.resize();
  }

  resize = () => {
   this.setState({scroll_size: window.innerWidth - 13 * 2});
  };

  handleClick = e => {
    var stage = e.currentTarget;
    var cursor = stage.getPointerPosition();
    var ratio = (cursor.x - 10) / (this.state.scroll_size -2);
    ratio = value_limit(ratio, 0, 1);
    this.setState({
     percentage: ratio
    });
    // console.log(this.state.percentage)

    this.props.setTime(ratio)
  };

  handleDrag = e => {
    var stage = e.currentTarget;
    var cursor = stage.getPointerPosition();
    var ratio = (cursor.x - 10) / (this.state.scroll_size -2);
    if (stage.onMouseUp) {
      ratio = value_limit(ratio, 0, 1);
      this.setState({
       percentage: ratio
      });
      // console.log(this.state.percentage)

      this.props.setTime(ratio)
      }
  };

  // #TODO: cannot detect scroll bar
  render() {
    const { scroll_size }= this.state;
    return (
      <Stage
        x={10}
        y={0}
        width={window.innerWidth}
        height={40}
        onMouseDown={this.handleClick}
        // onMouseMove={this.handleDrag}
      >
        <Layer>
          <Rect
            x = {0}
            y = {1}
            width={scroll_size}
            height={40-2}
            stroke={'black'}
            strokeWidth={2}

          />
          <Rect
            x = {1}
            y = {2}
            width={this.state.percentage * (scroll_size - 2)}
            height={40 - 4}
            fill={'blue'}
          />
        </Layer>
      </Stage>
    );
  }
}

export default Scroll;