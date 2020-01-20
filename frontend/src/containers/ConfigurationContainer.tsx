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
}

export interface ConfigurationContainerProp extends ContainerProps {
  updateConfiguration: (configuration: Types.Configuration) => void;
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
      error: ""
    };
  }

  updateConfiguration = async (configuration: Types.Configuration) => {
    // const { history } = this.props;
    await this.props.updateConfiguration(configuration);
    // history.push("/new-configuration/2");
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
