/** @jsx jsx */
import { jsx } from "@emotion/core";
import React from "react";
import { connect } from "react-redux";
import { withSnackbar, WithSnackbarProps } from "notistack";
import Tabs from "@material-ui/core/Tabs";
import Paper from "@material-ui/core/Paper";
import Tab from "@material-ui/core/Tab";
import { Switch, Route, Link } from "react-router-dom";
import { AppState } from "../redux-modules/root";
import { ContainerProps } from "./Container";
import * as Types from "../api/definitions";
import * as program from "../redux-modules/program";
import ProgramList from "../components/ProgramList";

export interface ConfigurationContainerState {
  isLoading: boolean;
  error: string;
  hasError: boolean;
}

export interface ConfigurationContainerProp
  extends ContainerProps,
    WithSnackbarProps {
  getPrograms: () => Promise<void>;
  createProgram: (program: Types.Program) => Promise<void>;
  updateProgram: (program: Types.Program) => Promise<void>;
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

  componentDidMount() {
    this.props.getPrograms();
    // this.props.fetchPrograms();
  }

  // updateConfiguration = async (configuration: Types.Configuration) => {
  //   try {
  //     this.setState({ isLoading: true });
  //     const response = await this.props.updateConfiguration(configuration);
  //     this.setState({
  //       isLoading: false,
  //       config_update_response: response
  //     });
  //   } catch (error) {
  //     this.setState({
  //       isLoading: false,
  //       config_update_response: "An error occured. Please try again."
  //     });
  //   }
  // };

  render() {
    const { program: programState, createProgram, updateProgram } = this.props;
    const programList = (programState && programState.programList) || [];
    const { match, location } = this.props;
    // const location = useLocation();

    return (
      <Switch>
        <Route path="/configuration">
          <React.Fragment>
            <Paper style={{ flexGrow: 1, marginTop: 30 }}>
              <Tabs value={location.pathname} centered>
                <Tab
                  label="Programs"
                  component={Link}
                  to={`${match.url}/programs`}
                  value={`${match.url}/programs`}
                />
                <Tab
                  label="Locations"
                  component={Link}
                  to={`${match.url}/locations`}
                  value={`${match.url}/locations`}
                />
                <Tab
                  label="Linking"
                  component={Link}
                  to={`${match.url}/Linking`}
                  value={`${match.url}/Linking`}
                />
              </Tabs>
            </Paper>
            <Switch>
              <Route path={`${match.url}/programs`}>
                <ProgramList
                  programList={programList}
                  {...this.state}
                  createProgram={createProgram}
                  updateProgram={updateProgram}
                />
              </Route>
              <Route path={`${match.url}/locations`}>
                <div>locations</div>
              </Route>
              <Route path={`${match.url}/linking`}>
                <div>linking</div>
              </Route>
              <Route path={`${match.url}`}>
                <div>Programs default page</div>
              </Route>
            </Switch>
          </React.Fragment>
        </Route>
      </Switch>
    );
  }
}

const mapStateToProps = (state: AppState) => {
  return {
    program: state.program
  };
};

const mapDispatchToProps = {
  getPrograms: program.actions.getPrograms,
  createProgram: program.actions.createProgram,
  updateProgram: program.actions.updateProgram
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(withSnackbar(ConfigurationContainer));
