/** @jsx jsx */
import React from "react";
import { jsx } from "@emotion/core";
// import { useHistory } from "react-router-dom";
import { Formik, ErrorMessage } from "formik";
import Button from "@material-ui/core/Button";
import Backdrop from "@material-ui/core/Backdrop";
import CircularProgress from "@material-ui/core/CircularProgress";
import {
  wrap,
  subHeading,
  fieldRow,
  selectField,
  mainContent,
  twoCol,
  inputField,
  label,
  fieldBox,
  backdrop,
  radioBox
} from "./styles";
import * as Types from "../api/definitions";

interface ProgramSelectionProps {
  client: Types.Client;
  programList: Types.Program[];
  onProgramSelect: (selected_program: string) => void;
  onLocationSelect: (selected_location: string) => void;
  submitPrediction: (client: Types.Client) => void;
  isLoading: boolean;
  hasError: boolean;
  error: string;
}

const ProgramSelection: React.FC<ProgramSelectionProps> = props => {
  // const changeProgram = (e: React.ChangeEvent<HTMLInputElement>) => {
  //   const value = e.currentTarget.value;
  //   props.onProgramSelect(value);
  // };

  const onLocationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const value = e.currentTarget.value;
    props.onLocationSelect(value);
  };

  const isChecked = (p: string, values: Types.Client) => {
    if (!values.program_type) {
      return false;
    }
    return p.toLowerCase() === values.program_type.toLowerCase();
  };

  return (
    <div css={wrap}>
      <div css={mainContent}>
        <Backdrop css={backdrop} open={props.isLoading}>
          <CircularProgress color="inherit" />
        </Backdrop>
        <h1 css={subHeading}>FM Prediction</h1>
        <Formik
          initialValues={props.client}
          enableReinitialize
          // validationSchema={Step2ValidationSchema}
          onSubmit={async (values, helpers) => {
            console.log(values);
            // add values to client state
            await props.submitPrediction(values);
            // helpers.resetForm();
          }}
        >
          {({
            values,
            handleSubmit,
            handleChange,
            handleBlur,
            touched,
            errors
          }) => (
            <form name="submitPredictionForm" onSubmit={handleSubmit}>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Program</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="Program"
                    readOnly
                    css={inputField}
                    placeholder=""
                    value={values.model_program || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="Program" />
                </div>
              </div>

              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>% Match</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="Confidence"
                    css={inputField}
                    placeholder=""
                    value={values.Confidence || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="Confidence" />
                </div>
              </div>
              <h1 css={subHeading}>Available Programs</h1>
              <div
                css={fieldRow}
                style={{ flexWrap: "wrap", marginBottom: 16 }}
              >
                {/*props.programList.length > 0 &&
                  props.programList.map(p => {
                    console.log(values.program_type);
                    console.log(p.program_name.toLowerCase());
                    return (
                      <div css={radioBox} key={p.program}>
                        <input
                          type="radio"
                          id={`id${p.program}`}
                          onChange={handleChange}
                          checked={
                            values.program_type
                              ? values.program_type.toLowerCase() ===
                                p.program_name.toLowerCase()
                              : false
                          }
                          name="program_type"
                          value={p.program_name}
                        />
                        <label htmlFor={`id${p.program}`}>
                          {p.program_name}
                        </label>
                      </div>
                    );
                  })*/}
                <div css={radioBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    checked={isChecked("ISM", values)}
                    id="ISM"
                    name="program_type"
                    value="ISM"
                  />
                  <label htmlFor="ISM">ISM</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("ISF", values)}
                    onChange={handleChange}
                    id="ISF"
                    name="program_type"
                    value="ISF"
                  />
                  <label htmlFor="ISF">ISF</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("MHFO", values)}
                    onChange={handleChange}
                    id="MHFO"
                    name="program_type"
                    value="MHFO"
                  />
                  <label htmlFor="MHFO">MHFO</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("SUBAB", values)}
                    onChange={handleChange}
                    value="SUBAB"
                    name="program_type"
                  />
                  <label htmlFor="SUBAB">SUBAB</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("DIAGNOSTIC", values)}
                    onChange={handleChange}
                    value="DIAGNOSTIC"
                    name="program_type"
                  />
                  <label htmlFor="DIAGNOSTIC">DIAGNOSTIC</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("SEXOF-MH", values)}
                    onChange={handleChange}
                    value="SEXOF-MH"
                    name="program_type"
                  />
                  <label htmlFor="SEXOF-MH">SEXOF-MH</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("SEXOF-SECURE", values)}
                    onChange={handleChange}
                    value="SEXOF-SECURE"
                    name="program_type"
                  />
                  <label htmlFor="SEXOF-SECURE">SEXOF-SECURE</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("SEXOF", values)}
                    onChange={handleChange}
                    value="SEXOF"
                    name="program_type"
                  />
                  <label htmlFor="SEXOF">SEXOF</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("ENHANCED", values)}
                    onChange={handleChange}
                    value="ENHANCED"
                    name="program_type"
                  />
                  <label htmlFor="ENHANCED">ENHANCED</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("SECURE-MALE", values)}
                    onChange={handleChange}
                    value="SECURE-MALE"
                    name="program_type"
                  />
                  <label htmlFor="SECURE-MALE">SECURE-MALE</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("SECURE-FEMALE", values)}
                    onChange={handleChange}
                    value="SECURE-FEMALE"
                    name="program_type"
                  />
                  <label htmlFor="SECURE-FEMALE">SECURE-FEMALE</label>
                </div>
                <div css={radioBox}>
                  <input
                    type="radio"
                    checked={isChecked("INDEPENDENT-LIVING", values)}
                    onChange={handleChange}
                    value="INDEPENDENT-LIVING"
                    name="program_type"
                  />
                  <label htmlFor="INDEPENDENT-LIVING">Independent Living</label>
                </div>
              </div>

              <div css={fieldRow} style={{ justifyContent: "flex-end" }}>
                <Button
                  type="submit"
                  size="large"
                  variant="contained"
                  color="primary"
                >
                  Get Locations
                </Button>
              </div>
            </form>
          )}
        </Formik>

        {props.client.SuggestedLocations &&
          props.client.SuggestedLocations.length > 0 && (
            <React.Fragment>
              <h1 css={subHeading}>Select Location</h1>
              <div css={fieldRow}>
                <select
                  css={selectField}
                  name="client_selected_location"
                  value={props.client.client_selected_locations || ""}
                  onChange={onLocationChange}
                >
                  <option value="">Select</option>
                  {props.client.SuggestedLocations.map(loc => (
                    <option key={loc} value={loc}>
                      {loc}
                    </option>
                  ))}
                </select>
              </div>
            </React.Fragment>
          )}
        {/*props.client.result_final && (
          <h1 css={subHeading}>{props.client.result_final}</h1>
        )*/}
      </div>
      {/* MAIN CONTENT */}
    </div>
  );
};

export default ProgramSelection;
