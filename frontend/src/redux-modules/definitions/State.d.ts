import * as Types from "../../api/definitions"; // CRA does not support abs paths for typescript yet.
import { FormikErrors } from "formik";
export interface ClientState {
  client: Types.Client;
  clientList: Types.Client[];
  errors: FormikErrors<Types.Client>;
}

export interface ConfigurationState {
  configuration: Types.Configuration;
}
