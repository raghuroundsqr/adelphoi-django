/** @jsx jsx */
import { jsx } from "@emotion/core";
// import { useHistory } from "react-router-dom";
import { Formik, ErrorMessage } from "formik";
import Button from "@material-ui/core/Button";
import { ConfigurationSchema } from "./ValidationSchema";
import {
  wrap,
  subHeading,
  fieldRow,
  mainContent,
  twoCol,
  inputField,
  label,
  txtDetail
} from "./styles";
import * as Types from "../api/definitions";

interface ConfigurationFormProps {
  configuration: Types.Configuration;
  onFormSubmit: (configuration: Types.Configuration) => void;
  isLoading: boolean;
  hasError: boolean;
  error: string;
  config_update_response: string | null;
}

const ConfigurationForm: React.FC<ConfigurationFormProps> = props => {
  // const history = useHistory();

  return (
    <div css={wrap}>
      <div css={mainContent}>
        <Formik
          initialValues={props.configuration}
          enableReinitialize
          validationSchema={ConfigurationSchema}
          onSubmit={async (values, helpers) => {
            await props.onFormSubmit(values);
          }}
        >
          {({ values, handleSubmit, handleChange }) => (
            <form name="newClientForm2" onSubmit={handleSubmit}>
              <h1 css={subHeading}>Program</h1>
              {props.config_update_response && (
                <div
                  css={txtDetail}
                  style={{ marginTop: 10, marginBottom: 10 }}
                >
                  {props.config_update_response}
                </div>
              )}
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Program</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="program"
                    css={inputField}
                    placeholder=""
                    value={values.program || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="program" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Program Name</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="program_name"
                    css={inputField}
                    placeholder=""
                    value={values.program_name || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="program_name" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Gender</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="gender"
                    css={inputField}
                    placeholder=""
                    value={values.gender || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="gender" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Gender name</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="gender_name"
                    css={inputField}
                    placeholder=""
                    value={values.gender_name || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="gender_name" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Level of care</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="level_of_care"
                    css={inputField}
                    placeholder=""
                    value={values.level_of_care || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="level_of_care" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Level names</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="level_names"
                    css={inputField}
                    placeholder=""
                    value={values.level_names || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="level_names" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Locations</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="location"
                    css={inputField}
                    placeholder=""
                    value={values.location || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="location" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Location names</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="location_names"
                    css={inputField}
                    placeholder=""
                    value={values.location_names || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="location_names" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Facility type</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="facility_type"
                    css={inputField}
                    placeholder=""
                    value={values.facility_type || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="facility_type" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Facility name</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="facility_names"
                    css={inputField}
                    placeholder=""
                    value={values.facility_names || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="facility_names" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Program model suggested</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="program_model_suggested"
                    css={inputField}
                    placeholder=""
                    value={values.program_model_suggested || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage
                    component="span"
                    name="program_model_suggested"
                  />
                </div>
              </div>
              <div css={fieldRow} style={{ justifyContent: "flex-end" }}>
                <Button
                  type="submit"
                  size="large"
                  variant="contained"
                  color="primary"
                >
                  Submit
                </Button>
              </div>
            </form>
          )}
        </Formik>
      </div>
      {/* MAIN CONTENT */}
    </div>
  );
};

export default ConfigurationForm;
