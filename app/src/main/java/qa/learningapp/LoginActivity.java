package qa.learningapp;

import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class LoginActivity extends AppCompatActivity {

  @BindView(R.id.editText_username) EditText editText_username;
  @BindView(R.id.editText_password) EditText editText_password;
  @BindView(R.id.textView_forgot) TextView textView_forgot;
  @BindView(R.id.button_login) Button button_login;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_login);
    ButterKnife.bind(this);
  }

  @OnClick(R.id.button_login)
  public void onClickLogin() {
    Snackbar.make(findViewById(android.R.id.content), "LOGIN CLICKED", Snackbar.LENGTH_SHORT).show();
  }

  @OnClick(R.id.textView_forgot)
  public void onClickForgot() {
    DialogFactory.error_toast(LoginActivity.this, "Ops! An Error Occurred").show();
  }
}
