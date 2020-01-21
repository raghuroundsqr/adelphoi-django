/** @jsx jsx */
import { jsx } from "@emotion/core";
import { useHistory } from "react-router-dom";
import { Formik, ErrorMessage } from "formik";
import Button from "@material-ui/core/Button";
import { Step2ValidationSchema } from "./ValidationSchema";
import {
  wrap,
  subHeading,
  fieldRow,
  flexRow,
  mainContent,
  twoCol,
  inputField,
  label,
  fieldBox
} from "./styles";
import * as Types from "../api/definitions";

interface PredictionFormStep2Props {
  client: Types.Client;
  onFormSubmit: (client: Types.Client) => void;
  isLoading: boolean;
  hasError: boolean;
  error: string;
}

const PredictionFormStep2: React.FC<PredictionFormStep2Props> = props => {
  const history = useHistory();

  return (
    <div css={wrap}>
      <div css={mainContent}>
        <Formik
          initialValues={props.client}
          enableReinitialize
          validationSchema={Step2ValidationSchema}
          onSubmit={async (values, helpers) => {
            console.log("submtting the form on step2");
            console.log(values);
            // add values to client state
            await props.onFormSubmit(values);
            // await this.onFormSubmit(currentQuestion, values);
            helpers.resetForm();
          }}
        >
          {({ values, handleSubmit, handleChange }) => (
            <form name="newClientForm2" onSubmit={handleSubmit}>
              <h1 css={subHeading}>Assessment Scores</h1>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>YLS Family Circumstances Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="yls_FamCircumstances_Score"
                    css={inputField}
                    placeholder=""
                    value={values.yls_FamCircumstances_Score || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage
                    component="span"
                    name="yls_FamCircumstances_Score"
                  />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>YLS Education/Employment Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="yls_Edu_Employ_Score"
                    css={inputField}
                    placeholder=""
                    value={values.yls_Edu_Employ_Score || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="yls_Edu_Employ_Score" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>YLS Peer Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="yls_Peer_Score"
                    css={inputField}
                    placeholder=""
                    value={values.yls_Peer_Score || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="yls_Peer_Score" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>YLS Subab Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="yls_Subab_Score"
                    css={inputField}
                    placeholder=""
                    value={values.yls_Subab_Score || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="yls_Subab_Score" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>YLS Leisure Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="yls_Leisure_Score"
                    css={inputField}
                    placeholder=""
                    value={values.yls_Leisure_Score || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="yls_Leisure_Score" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>YLS Personality Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="yls_Personality_Score"
                    css={inputField}
                    placeholder=""
                    value={values.yls_Personality_Score || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="yls_Personality_Score" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>YLS Attitude Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="yls_Attitude_Score"
                    css={inputField}
                    placeholder=""
                    value={values.yls_Attitude_Score || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="yls_Attitude_Score" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>YLS Prior/Current Offenses Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="yls_PriorCurrentOffenses_Score"
                    css={inputField}
                    placeholder=""
                    value={values.yls_PriorCurrentOffenses_Score || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage
                    component="span"
                    name="yls_PriorCurrentOffenses_Score"
                  />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Family Support</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="family_support"
                    css={inputField}
                    placeholder=""
                    value={values.family_support || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="family_support" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Fire Setting</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="fire_setting"
                    css={inputField}
                    placeholder=""
                    value={values.fire_setting || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="fire_setting" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Level of Aggression</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="level_of_aggression"
                    css={inputField}
                    placeholder=""
                    value={values.level_of_aggression || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="level_of_aggression" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Self-Harm</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="client_self_harm"
                    css={inputField}
                    placeholder=""
                    value={values.client_self_harm || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="client_self_harm" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Trauma Assessment Score</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="Screening_tool_Trauma"
                    css={inputField}
                    placeholder=""
                    value={values.Screening_tool_Trauma || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="Screening_tool_Trauma" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>CANS Life Functioning</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="cans_LifeFunctioning"
                    css={inputField}
                    placeholder=""
                    value={values.cans_LifeFunctioning || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="cans_LifeFunctioning" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>CANS Youth Strengths</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="cans_YouthStrengths"
                    css={inputField}
                    placeholder=""
                    value={values.cans_YouthStrengths || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="cans_YouthStrengths" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>CANS Caregiver Strengths</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="cans_CareGiverStrengths"
                    css={inputField}
                    placeholder=""
                    value={values.cans_CareGiverStrengths || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage
                    component="span"
                    name="cans_CareGiverStrengths"
                  />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>CANS Culture</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="cans_Culture"
                    css={inputField}
                    placeholder=""
                    value={values.cans_Culture || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="cans_Culture" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>CANS Youth Behavior</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="cans_YouthBehavior"
                    css={inputField}
                    placeholder=""
                    value={values.cans_YouthBehavior || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="cans_YouthBehavior" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>CANS Youth Risk</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="cans_YouthRisk"
                    css={inputField}
                    placeholder=""
                    value={values.cans_YouthRisk || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="cans_YouthRisk" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>CANS Trauma Experience</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="cans_Trauma_Exp"
                    css={inputField}
                    placeholder=""
                    value={values.cans_Trauma_Exp || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="cans_Trauma_Exp" />
                </div>
              </div>
              <h1 css={subHeading}>Referred Program</h1>
              <div css={flexRow} style={{ flexWrap: "wrap", marginBottom: 16 }}>
                {/** style={{ flexWrap: "wrap", marginBottom: 16 }} */}
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    id="ISM"
                    name="referred_program"
                    value="ISM"
                  />
                  <label htmlFor="ISM">ISM</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    id="ISF"
                    name="referred_program"
                    value="ISF"
                  />
                  <label htmlFor="ISF">ISF</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    id="MHFO"
                    name="referred_program"
                    value="MHFO"
                  />
                  <label htmlFor="MHFO">MHFO</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="SUBAB"
                    name="referred_program"
                  />
                  <label htmlFor="SUBAB">SUBAB</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="Diagnostic"
                    name="referred_program"
                  />
                  <label htmlFor="Diagnostic">Diagnostic</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="SEXOF-MH"
                    name="referred_program"
                  />
                  <label htmlFor="SEXOF-MH">SEXOF-MH</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="SEXOF-Secure"
                    name="referred_program"
                  />
                  <label htmlFor="SEXOF-Secure">SEXOF-Secure</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="SEXOF"
                    name="referred_program"
                  />
                  <label htmlFor="SEXOF">SEXOF</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="Enhanced"
                    name="referred_program"
                  />
                  <label htmlFor="Enhanced">Enhanced</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="Secure-Male"
                    name="referred_program"
                  />
                  <label htmlFor="Secure-Male">Secure-Male</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="Secure-Female"
                    name="referred_program"
                  />
                  <label htmlFor="Secure-Female">Secure-Female</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    value="Independent-Living"
                    name="referred_program"
                  />
                  <label htmlFor="Independent-Living">Independent Living</label>
                </div>
              </div>
              <div css={fieldRow} style={{ justifyContent: "flex-end" }}>
                <Button
                  type="button"
                  variant="contained"
                  size="large"
                  style={{ marginRight: 10 }}
                  onClick={() => history.push("/new-client")}
                >
                  Previous
                </Button>
                <Button
                  type="submit"
                  size="large"
                  variant="contained"
                  color="primary"
                >
                  Submit For FirstMatch Prediction
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

export default PredictionFormStep2;
