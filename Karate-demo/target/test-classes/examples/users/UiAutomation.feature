Feature:Google Search


Scenario: Health care automation
    * configure driver = {type:'chrome'}
    Given driver "https://katalon-demo-cura.herokuapp.com/"
    And waitFor("#btn-make-appointment")
    * screenshot()
    And click("#btn-make-appointment")
    And waitFor("#txt-username")
    * screenshot()
    And input("#txt-username","John Doe")
    And input("#txt-password","ThisIsNotAPassword")
    And click("#btn-login")
    * delay(700)
    * screenshot()
    And input("#txt_visit_date","24/06/2021")
    And click("#txt_comment")
    And input("#txt_comment","sample comment")
    * screenshot()
    And click("#btn-book-appointment")
    * delay(10000)
    * screenshot()
