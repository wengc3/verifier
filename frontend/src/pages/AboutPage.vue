<template>
  <div>
    <v-btn flat blue :to="{ name: 'home'}"><v-icon>mdi-arrow-left-bold-circle</v-icon> Home</v-btn>
    <v-container>
      <h2 class="my-3">Next Generation E-Voting</h2>
      <p>With our application, it is possible to conduct election events according to the protocol specifications not only from the perspective of a voter, but also all other participating actors such as the election administrator, printing, or election authority, offering a preview of how the future of voting might possibly look like in Switzerland.</p>
      <p>The "CHVote System Specifications" (the cryptographic specifications this application is based on), can be found here: <a href="https://eprint.iacr.org/2017/325">https://eprint.iacr.org/2017/325</a></p>
      <h3>Version 1.0</h3>
      <p>This application is the result of the bachelor thesis "Visualizing Geneva's Next E-Voting System" and has been realized by <strong>Kevin Häni</strong> and <strong>Yannick Denzer</strong>.</p>
      <p>The full source code of this application is available on GitHub: <a href="https://github.com/nextgenevoting">https://github.com/nextgenevoting</a></p>

      <h3>Version 1.1</h3>
      <p>This application is the result of the bachelor thesis "Universelle Verifizierung des Genfer E-Voting Systems" and has been realized by <strong>Christian Wenger</strong>. The new feature is a fully implemented Verfier. The reason of the skipped results is because of the missing signaturs and certificates. </p>
      <p>The full source code of this application is available on GitHub: <a href="https://gitlab.ti.bfh.ch/chvote/verifier">https://gitlab.ti.bfh.ch/chvote/verifier</a></p>
    </v-container>
  </div>
</template>
