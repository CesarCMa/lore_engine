import clsx from 'clsx';

export default function Card({ children, className, title, footer }) {
  return (
    <div
      className={clsx(
        'bg-parchment-100 border-2 border-gold-500 rounded-lg p-6 shadow-parchment',
        className
      )}
    >
      {title && (
        <div className="border-b border-gold-300 pb-3 mb-4">
          <h3 className="font-heading text-xl text-arcane-700">{title}</h3>
        </div>
      )}

      <div>{children}</div>

      {footer && (
        <div className="border-t border-gold-300 pt-3 mt-4">
          {footer}
        </div>
      )}
    </div>
  );
}
