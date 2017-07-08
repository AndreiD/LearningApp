package qa.learningapp;

import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.SeekBar;
import android.widget.Spinner;
import android.widget.TextView;
import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class MainActivity extends AppCompatActivity {

  private TextView mTextMessage;
  @BindView(R.id.button_press_me) Button button_press_me;
  @BindView(R.id.textView_weather) TextView textView_weather;
  @BindView(R.id.spinner_id_342) Spinner spinner_id_342;
  @BindView(R.id.editText_username) EditText editText_username;
  @BindView(R.id.checkbox_main) CheckBox checkbox_main;
  @BindView(R.id.radio_button_1) RadioButton radio_button_1;
  @BindView(R.id.radio_button_2) RadioButton radio_button_2;
  @BindView(R.id.seekbar_one) SeekBar seekbar_one;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    ButterKnife.bind(this);

    new CountDownTimer(4000,4000){

      @Override
      public void onTick(long l) {

      }

      @Override
      public void onFinish() {
        textView_weather.setText("Weather in Sofia: 38 degrees");
      }
    }.start();
  }

  @Override
  public boolean onCreateOptionsMenu(Menu menu) {
    MenuInflater menuInflater = getMenuInflater();
    menuInflater.inflate(R.menu.navigation, menu);
    return true;
  }

  @OnClick(R.id.button_press_me) public void onClickMainButton(){
    DialogFactory.createSimpleOkDialog(this,"Button was clicked","press ok to continue...").show();
  }

  public boolean onOptionsItemSelected(MenuItem item) {

    switch (item.getItemId()) {
      case R.id.menu_settings:
        startActivity(new Intent(MainActivity.this, SettingsActivity.class));
        return true;

      default:
        return super.onOptionsItemSelected(item);
    }
  }
}
