import pytest

class TestMock():
    def test_mocking(self,calculator_with_mock,mock_history):
        result = calculator_with_mock.add(1,2)
        mock_history.log.assert_called_once_with("1 + 2", 3)

    def test_multiple_calls_tracked(self, calculator_with_mock, mock_history):                                                                           
      """Verify mock tracks all calls, not just one."""                                                                                                
      # Call 3 different operations
      calculator_with_mock.add(1, 1)                                                                                                                   
      calculator_with_mock.multiply(2, 2)
      calculator_with_mock.substract(5, 3)                                                                                                             
                                                                                                                                                       
      # Verify all 3 were logged
      assert mock_history.log.call_count == 3                                                                                                          
      # [Your assertions here for the actual calls]
      calls = mock_history.log.call_args_list
      assert calls[0][0] == ("1 + 1", 2)     
      assert calls[1][0] == ("2 * 2", 4)                                                                                                                   
      assert calls[2][0] == ("5 - 3", 2)


    def test_no_history_call(self,calculator_with_mock,mock_history):
        """Divide by zero fails, history should NOT be logged."""    

        try:                                                                                                                                             
          calculator_with_mock.divide(10, 0)                                                                                                           
        except ValueError:                                                                                                                               
          pass                                                                                                                                         
  
      # Verify history.log was never called                                                                                                            
        mock_history.log.assert_not_called()

    def test_side_effects(self,calculator_with_mock,mock_history):
        """Simulate history service failing (mock raises exception)."""
      # Make log() raise an exception when called                                                                                                      
        mock_history.log.side_effect = Exception("Database offline!") 
    

      # When calculator tries to log, the mock raises                                                                                                  
        with pytest.raises(Exception, match="Database offline"):
          calculator_with_mock.add(1, 2)   


        


         

