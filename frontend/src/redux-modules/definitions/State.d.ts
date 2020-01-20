import * as Types from "../../api/definitions"; // CRA does not support abs paths for typescript yet.

export interface ClientState {
  client: Types.Client;
  clientList: Types.Client[];
}

export interface ConfigurationState {
  configuration: Types.Configuration;
}
