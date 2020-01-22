import React from "react";
import { connect } from "react-redux";
import { Switch, Route } from "react-router-dom";
import { AppState } from "../redux-modules/root";
import { ContainerProps } from "./Container";
import * as configuration from "../redux-modules/configuration";
import ConfigurationForm from "../components/ConfigurationForm";
import * as Types from "../api/definitions";

export interface ConfigurationContainerState {
  isLoading: boolean;
  error: string;
  hasError: boolean;
  config_update_response: string | null;
}

export interface ConfigurationContainerProp extends ContainerProps {
  updateConfiguration: (configuration: Types.Configuration) => Promise<string>;
}

export class ConfigurationContainer extends React.Component<
  ConfigurationContainerProp,
  ConfigurationContainerState
> {
  constructor(props: ConfigurationContainerProp) {
    super(props);
    this.state = this.getInitialState();
  }
  getInitialState() {
    return {
      isLoading: false,
      hasError: false,
      error: "",
      config_update_response: null
    };
  }

  updateConfiguration = async (configuration: Types.Configuration) => {
    try {
      this.setState({ isLoading: true });
      const response = await this.props.updateConfiguration(configuration);
      this.setState({
        isLoading: false,
        config_update_response: response
      });
    } catch (error) {
      this.setState({
        isLoading: false,
        config_update_response: "An error occured. Please try again."
      });
    }
  };

  render() {
    const { configuration: configurationState } = this.props;
    let currentConfiguration: Types.Configuration;
    currentConfiguration = configurationState
      ? configurationState.configuration
      : Types.emptyConfiguration;

    return (
      <Switch>
        <Route exact path="/configuration">
          <ConfigurationForm
            configuration={currentConfiguration}
            {...this.state}
            onFormSubmit={this.updateConfiguration}
          />
        </Route>
      </Switch>
    );
  }
}

const mapStateToProps = (state: AppState) => {
  return {
    configuration: state.configuration
  };
};

const mapDispatchToProps = {
  updateConfiguration: configuration.actions.updateConfiguration
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ConfigurationContainer);
