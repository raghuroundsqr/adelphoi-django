App is developed using typescript, react, react router 5 and redux. All versions are latest by Feb 2020.
Emotion 10 used for styling the app.

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

Core directories
Api

- api.ts
- definitions
  redux-modules
- follows ducks pattern to contain reducer, actions and selectors in a single file.
  Containers
- connected components that interact with redux state. Also contains Routes wherever required
  Components
- presentational components used by containers
  App.ts - bootstraps the app

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (Webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

## Deploy

Make sure latest code is pushed to master branch.
(assumes key.pem is in the same directory)

1. ssh -i "key.pem" ubuntu@xx.xxx.xx.x
2. cd /var/www/adelphoi-django/
3. git pull
4. cd frontend
5. yarn build

## Third party packages

1. Form handling - Formik
2. Styles (css-in-js) - Emotion 10
3. Material UI React
4. React Select
